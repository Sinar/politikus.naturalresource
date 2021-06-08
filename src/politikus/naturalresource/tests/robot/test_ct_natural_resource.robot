# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s politikus.naturalresource -t test_natural_resource.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src politikus.naturalresource.testing.POLITIKUS_NATURALRESOURCE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/politikus/naturalresource/tests/robot/test_natural_resource.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Natural Resource
  Given a logged-in site administrator
    and an add Natural Resource form
   When I type 'My Natural Resource' into the title field
    and I submit the form
   Then a Natural Resource with the title 'My Natural Resource' has been created

Scenario: As a site administrator I can view a Natural Resource
  Given a logged-in site administrator
    and a Natural Resource 'My Natural Resource'
   When I go to the Natural Resource view
   Then I can see the Natural Resource title 'My Natural Resource'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Natural Resource form
  Go To  ${PLONE_URL}/++add++Natural Resource

a Natural Resource 'My Natural Resource'
  Create content  type=Natural Resource  id=my-natural_resource  title=My Natural Resource

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Natural Resource view
  Go To  ${PLONE_URL}/my-natural_resource
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Natural Resource with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Natural Resource title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
