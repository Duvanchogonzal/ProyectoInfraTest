pipeline {
    agent any

    stages {
        stage('Build Backend Image') {
            steps {
                sh 'docker build -t miapp:latest ./app'
            }
        }

        stage('Build Nginx Image') {
            steps {
                sh 'docker build -t mininginx:latest ./nginx'
            }
        }

        stage('List Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
