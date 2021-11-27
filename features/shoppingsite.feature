Feature: Testing e-commerce Wishlist Search and Cart Functions

  Testing e-commerce Wishlist Search and Cart Functions

  Scenario: wishlist search and cart functions check
    Given I add four different products to my wish list
    When I view my wishlist table
    Then I find total selected items in my Wishlist
    When I search for lowest price product
    And I am able to add the lowest price item to my cart
    Then I am able to verify the item in my cart