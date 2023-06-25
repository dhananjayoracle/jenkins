pipeline {
    agent any
    environment{
        check:"cheking"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh "python3 sample.py"
            }
        }
        stage('Deploy') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}