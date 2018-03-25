Feature: Validate the functionalities for my site

@navigateHomePage
Scenario: I would hit the url and verify the title
  Given I visit the url "https://soumyajit2016.wordpress.com/"
  Then I verify the title of the home page

@navigateAboutPage
Scenario: I would navigate to about my page and verify the title
  Then I navigate to About My page
  Then I verify the title of the about me page

@navigateGitHubPage
Scenario: I would navigate to GitHub and verify the title
  Then I navigate to GitHub page
  Then I verify the title of the GitHub page

@navigateBitbucketPage
Scenario: I would navigate to Bitbucket and verify the title
  Then I navigate to Bitbucket page
  Then I verify the title of the Bitbucket page

@navigateFacebookPage
Scenario: I would navigate to Facebook and verify the title
  Then I navigate to Facebook page
  Then I verify the title of the Facebook page

@navigateLinkedinPage
Scenario: I would navigate to LinkedIn and verify the title
  Then I navigate to Linkedin page
  Then I verify the title of the Linkedin page

@navigateTwitterPage
Scenario: I would navigate to Twitter and verify the title
  Then I navigate to Twitter page
  Then I verify the title of the Twitter page
