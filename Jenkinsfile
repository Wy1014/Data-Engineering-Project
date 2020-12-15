pipeline{
  agent any
  stages {
    stage('Build Flask app'){
      steps{
        script{
          if(env.BRANCH_NAME == 'main' || env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'feature'){
            sh 'docker build -t project .'
          }
        }      
      }
    }
    stage('Run docker images'){
      parallel{
        stage('Run Flask App'){
          steps{
            script{
              if(env.BRANCH_NAME == 'main' || env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'feature'){
                sh 'docker run -d -p 5000:5000 --name project_c project'
              }  
            }
          }
        }
      }
    }
    stage('Testing'){
      steps{
        script{
          if(env.BRANCH_NAME == 'main'){
            sh 'python stress_test.py'
          }
          else if(env.BRANCH_NAME == 'develop'){
            echo 'develop-specific test'
          }
          else if(env.BRANCH_NAME == 'feature'){
            echo 'feature-specific test'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if(env.BRANCH_NAME == 'main'){
            sh 'docker rm -f project_c'
            sh 'docker rmi -f project'
          }
        }
      }
    }
    stage('Creating develop branch'){
      steps{
        script{
          if(env.BRANCH_NAME == 'main'){
            echo 'branch into develop'
          }
        }
      }
    }
    stage('Creating feature branch'){
      steps{
        script{
          if(env.BRANCH_NAME == 'main'){
            echo 'branch into feature'
          }
        }
      }
    }
  }  
}
