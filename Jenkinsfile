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
                    println write_status
                }
            }
        }
    }
}