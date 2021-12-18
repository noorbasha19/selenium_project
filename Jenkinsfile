pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                bat '''
                ls
                cd ${WORKSPACE}
                pip install pytest
                '''
            }
        }

    }
}