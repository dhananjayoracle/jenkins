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
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh "echo ${Hello}"
            }
        }
    }
}