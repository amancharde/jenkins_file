pipeline
{
  agent any;
  stages
  {
    stage('build')
    {
      steps
      {
        print("hello")
      }
    }
  }
}
