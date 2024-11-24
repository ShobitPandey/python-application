pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'  // Use Jenkins credentials ID
        IMAGE_NAME = 'my-python-app'
        DOCKER_HUB_REPO = 'your-dockerhub-username/my-python-app'
    }
    stages {
        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use Jenkins credentials for Docker login
                    docker.withRegistry('', DOCKER_HUB_CREDENTIALS) {
                        echo 'Logged in to Docker Hub'
                    }
                }
            }
        }
        // Other stages (build, push) follow here...
    }
}
