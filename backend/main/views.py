from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import VideoAnalysisSerializer
from .models import VideoAnalysis
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import numpy as np
import cv2
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import Xception
from django.conf import settings

# Parameters
frame_height, frame_width = 160, 160  # Frame dimensions
sequence_length = 10  # Number of frames to consider in a sequence
num_classes = 2  # Number of classes (Real or Fake)

class VideoAnalysisList(generics.ListCreateAPIView):
    queryset = VideoAnalysis.objects.all()
    serializer_class = VideoAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoAnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoAnalysis.objects.all()
    serializer_class = VideoAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]

def load_xception_model():
    """Load the Xception model for feature extraction without the top layer."""
    base_model = Xception(include_top=False, input_shape=(frame_height, frame_width, 3), pooling='avg')
    return base_model

def load_single_video(video_file, xception_model):
    """Extract frames from the video and generate embeddings using Xception model."""
    cap = cv2.VideoCapture(video_file)
    embeddings = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (frame_height, frame_width))
        frame = frame / 255.0  # Normalize frame
        embedding = xception_model.predict(np.expand_dims(frame, axis=0))
        embeddings.append(embedding.flatten())  # Flatten the embeddings
    
    cap.release()

    # Ensure the sequence has the required length (pad if necessary)
    while len(embeddings) < sequence_length:
        embeddings.append(embeddings[-1])  # Duplicate the last frame if needed

    return np.array(embeddings) if embeddings else None

def create_model():
    """Create and compile the LSTM model for video classification."""
    model = Sequential()
    model.add(LSTM(128, return_sequences=False, input_shape=(sequence_length, 2048)))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

@csrf_exempt
def detect_deepfake(request):
    """Handle video uploads and perform deepfake detection."""
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']

        # Validate file extension
        valid_extensions = ['.mp4', '.avi', '.mov']
        if not any(video_file.name.endswith(ext) for ext in valid_extensions):
            return JsonResponse({'error': 'Unsupported file type'}, status=400)

        # Save the uploaded video file
        video_path = default_storage.save(f'videos/{video_file.name}', video_file)

        # Load models if not already loaded
        global xception_model
        global detection_model
        if 'xception_model' not in globals():
            xception_model = load_xception_model()
        if 'detection_model' not in globals():
            detection_model = create_model()
            detection_model.load_weights(r'C:\\Users\\boddu\\Desktop\\Project\\deepfake\\backend\\deepfake_detect_model.h5')

        # Path to the uploaded video file
        full_video_path = os.path.join(settings.MEDIA_ROOT, video_path)

        # Extract frames and compute embeddings
        frames = load_single_video(full_video_path, xception_model)
        if frames is not None:
            frames = np.expand_dims(frames, axis=0)
            prediction = detection_model.predict(frames)
            class_label = np.argmax(prediction)  # 0 for Real, 1 for Fake
            prediction_probabilities = prediction[0]

            # Store analysis result in the database
            analysis = VideoAnalysis(
                video=video_file,
                result=class_label,  # 0: Real, 1: Fake
                confidence_real=prediction_probabilities[0],  # Confidence for real
                confidence_fake=prediction_probabilities[1],  # Confidence for fake
            )
            analysis.save()

            # Serialize the analysis result
            serializer = VideoAnalysisSerializer(analysis)
            result = serializer.data
        else:
            result = {'error': 'Could not process the video'}

        return JsonResponse(result)

    return JsonResponse({'error': 'Invalid request method or missing video file'})
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from . import models

class UserList(generics.ListCreateAPIView):
    queryset = models.USER.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = models.USER.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    
    
