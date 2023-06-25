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
                    
                    def lines = readFile(file: "tmp_alias_output").split('\n')
                    print(lines)
                    

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