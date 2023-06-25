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
                    
                    def lines = readFile(file: "tmp_output").split('\n')
                    for (line in lines)
                    {
                        println (line)
                    }
                    sh "echo ${Hello}"
                    

                }
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: '312ba97a-c773-41c0-ba8c-3044af7d4076', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh "echo ${user} ${pass}"

                }
            }
        }
    }
}