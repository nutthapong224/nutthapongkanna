pipeline {
    agent any

    environment {
        IMAGE_NAME = "ghcr.io/nutthapong224/testbdi/hello-ci:latest"
        CONTAINER_NAME = "hello-ci-container"
    }

    stages {
        stage('Pull Docker Image') {
            steps {
                echo "Pulling image from GHCR (public)..."
                sh "docker pull ${IMAGE_NAME}"
            }
        }

        stage('Stop Old Container if Exists') {
            steps {
                script {
                    sh '''
                    if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
                        echo "Stopping and removing old container..."
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    fi
                    '''
                }
            }
        }

        stage('Approval for Staging') {
            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    script {
                        input message: 'ต้อง กด Approve ก่อนรัน Deploy to Staging', 
                              ok: 'อนุมัติ' 
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                echo "Running container (dummy)..."
                docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME} tail -f /dev/null
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Checking all containers (including stopped ones)..."
                sh 'docker ps -a'
            }
        }

        stage('Run Python Test') {
            steps {
                echo "Running unit test for say_hello()..."
                sh '''
                docker exec ${CONTAINER_NAME} pytest /app/tests/test_hello.py
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment and tests successful!"
        }
        failure {
            echo "❌ Deployment or tests failed!"
        }
    }
}
