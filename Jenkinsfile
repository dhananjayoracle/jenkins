pipeline {
    agent any
    environment{
        Hello="hello"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                script{
                    write_status = sh (
                            script: 'python3 sample.py > tmp_output',
                            returnStdout: true
                        ).trim()
                    
                    
                }
            }
        }
        stage('Deploy') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}