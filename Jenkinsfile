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
                    println "Hello ${write_status}"
                    slackSend(channel: "${slackChannel}",
                                        color: "danger",
                                        message: """${env.JOB_NAME} job id ${currentBuild.number} has Failed, Full log > ${env.BUILD_URL}consoleText
                                        Last commit message: '${env.GIT_COMMIT_MSG}'
                                        Comitted by: ${env.GIT_AUTHOR}
                                        Job: ${env.JOB_NAME}
                                        Build #${env.BUILD_NUMBER}
                                        Message: # "Hello from jenkins" ,
                                        teamDomain: 'dyn', token: "${slackChannelToken}""")
                }
            }
        }
    }
}