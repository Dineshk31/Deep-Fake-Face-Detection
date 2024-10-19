import React from 'react';
import { Card, Container, Button } from 'react-bootstrap';
import { FaCheckCircle, FaUsers, FaCode, FaLightbulb } from 'react-icons/fa'; // Importing icons

function AboutUs() {
    return (
        <Container className="mt-5">
            <h2 className="text-center mb-4" style={{ fontWeight: 'bold', color: '#ffc107' }}>DEEPFAKE DETECTION SYSTEM</h2>

            <Card className="p-4 shadow-lg" style={{ backgroundColor: '#212529', border: '2px solid #ffc107', borderRadius: '10px' }}>
                <Card.Body>
                    <h3 className="text-light">Hello! We are LinkedIn Park</h3>
                    <p className="text-white">
                        We are a bunch of tech enthusiasts who want to make a difference in the real world. We came across many problem statements, but we chose to tackle one that can truly help people. Providing a solution to a real-world problem with technology has never been more crucial. Deepfakes are everywhere, from celebrity impersonations to memes. While creating them can be entertaining, misusing someone's identity is not just a joke—it's identity theft! We have integrated our specialized technology to tackle this issue using various Deep Learning Models like CNN and Facenet. After extensive research, we found that XceptionNet was the best model for our needs. We trained our model with existing datasets like Face Forensics++ and created our own deepfakes. To our surprise, it took only minutes to replicate someone else's appearance! We also guide users to report any deepfake incidents to Cyber Crime if they discover something suspicious. All our hard work is worth it because we created one of the most effective DeepFake Detectors out there!
                    </p>

                    <h3 className="text-light">Problem Statement</h3>
                    <p className="text-white">
                        Deepfakes refer to synthetic media where a person's likeness is manipulated to create realistic-looking but fake content. This technology poses significant risks, including misinformation, identity theft, and reputational damage. With the rise of deepfake videos, distinguishing between authentic and manipulated content has become increasingly challenging for individuals and organizations alike.
                    </p>

                    <h3 className="text-light">Solution Approach</h3>
                    <p className="text-white">
                        Our Deepfake Detection System utilizes advanced machine learning algorithms and artificial intelligence to analyze video content effectively. By employing deep learning techniques, our system aims to identify signs of manipulation and provide reliable results to users. The approach includes:
                    </p>
                    <ul className="text-white">
                        <li><FaCheckCircle className="text-success" /> <strong>Data Collection:</strong> Gathering a diverse dataset of both real and deepfake videos to train our models.</li>
                        <li><FaCheckCircle className="text-success" /> <strong>Feature Extraction:</strong> Analyzing video frames for inconsistencies that are often present in deepfakes.</li>
                        <li><FaCheckCircle className="text-success" /> <strong>Model Training:</strong> Using state-of-the-art algorithms to improve detection accuracy through iterative training.</li>
                        <li><FaCheckCircle className="text-success" /> <strong>User-Friendly Interface:</strong> Providing an intuitive interface for users to easily upload and analyze videos.</li>
                    </ul>

                    <h3 className="text-light">Our Goals</h3>
                    <p className="text-white">
                        We aim to:
                    </p>
                    <ul className="text-white">
                        <li><FaUsers className="text-info" /> Enhance digital literacy regarding deepfakes and their implications.</li>
                        <li><FaUsers className="text-info" /> Provide individuals and organizations with tools to combat misinformation.</li>
                        <li><FaUsers className="text-info" /> Collaborate with law enforcement and cybersecurity experts to tackle the growing threat of deepfakes.</li>
                    </ul>

                    <h3 className="text-light">Our Team</h3>
                    <p className="text-white">
                        Our dedicated team consists of experts in AIML, WEB DEVELOPMENT, and more. We work collaboratively to ensure our technology remains at the forefront of deepfake detection.
                    </p>
                    <ul className="text-white">
                        <li><FaCode className="text-warning" /> <strong>V Dinesh:</strong> Machine Learning </li>
                        <li><FaCode className="text-warning" /> <strong>B Sriram:</strong> Web Development</li>
                        <li><FaCode className="text-warning" /> <strong>N Murali:</strong> Web Development</li>
                        <li><FaCode className="text-warning" /> <strong>P Tejesh:</strong> Machine Learning</li>
                    </ul>

                    <h3 className="text-light">Technologies Used</h3>
                    <p className="text-white">
                        Our system is built using the following technologies:
                    </p>
                    <ul className="text-white">
                        <li><FaLightbulb className="text-primary" /> <strong>Machine Learning Frameworks:</strong> TensorFlow</li>
                        <li><FaLightbulb className="text-primary" /> <strong>Programming Languages:</strong> Python, JavaScript</li>
                        <li><FaLightbulb className="text-primary" /> <strong>Frontend Technologies:</strong> React, Bootstrap</li>
                        <li><FaLightbulb className="text-primary" /> <strong>Backend Technologies:</strong> Django</li>
                    </ul>

                    <h3 className="text-light">Future Plans</h3>
                    <p className="text-white">
                        We aim to continually enhance our system's capabilities by:
                    </p>
                    <ul className="text-white">
                        <li><FaCheckCircle className="text-success" /> Incorporating more advanced AI algorithms to improve detection accuracy.</li>
                        <li><FaCheckCircle className="text-success" /> Expanding our dataset to cover more diverse scenarios and types of deepfakes.</li>
                        <li><FaCheckCircle className="text-success" /> Launching a public awareness campaign to educate users about deepfakes.</li>
                    </ul>

                    <h3 className="text-light">Contact Us</h3>
                    <p className="text-white">
                        For inquiries, collaborations, or to report a deepfake, please contact us at: 
                        <Button 
                            variant="info" 
                            href="https://park-portfolio.netlify.app/" 
                            className="ml-2"
                        >
                            Click Here
                        </Button>
                    </p>
                </Card.Body>
            </Card>
        </Container>
    );
}

export default AboutUs;
