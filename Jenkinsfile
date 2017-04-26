pipeline {
  agent any
  stages {
    stage('scm') {
      steps {
        sh 'echo $WORK_SPACE'
        timeout(time: 10) {
          sleep 5
        }
        
      }
    }
    stage('build') {
      steps {
        ws(dir: 'submodule') {
          writeFile(file: 'deploy.txt', text: 'hello')
        }
        
      }
    }
  }
}