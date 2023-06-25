pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '312ba97a-c773-41c0-ba8c-3044af7d4076', url: 'https://github.com/dhananjayoracle/jenkins.git']])
            }
        }
        stage('Built'){
            steps{
                git branch: 'main', credentialsId: '312ba97a-c773-41c0-ba8c-3044af7d4076', url: 'https://github.com/dhananjayoracle/jenkins.git'
                sh 'python3 sample.py'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing 1 2 3 '
            }
        }
    }
}
