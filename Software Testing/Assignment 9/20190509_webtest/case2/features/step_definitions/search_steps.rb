Given /^I am on the (.+) Home Page$/ do |site|
  @site = site.downcase
  visit @site, :home_page
end

When /^I search for a? ?"([^"]*)"$/ do |term|
  on @site, :home_page do |page|
    page.search_for term
  end
end

When /^I search for a?n? ?([^"].+[^"])$/ do |term|
  term = Common.get_search_term_data term
  on @site, :home_page do |page|
    page.search_for term
  end
end

Then /^I should see at least ([\d,]+) results$/ do |exp_num_results|
  on @site, :results_page do |page|
    page.number_search_results.should >= exp_num_results.gsub(",","").to_i
  end
end

Then /^I should see at most ([\d,]+) results$/ do |exp_num_results|
  on @site, :results_page do |page|
    page.number_search_results.should <= exp_num_results.gsub(",","").to_i
  end
end

When /^I translate (.+)$/ do |translation_statement|
  on @site, :home_page do |page|
    page.search_for "translate #{translation_statement}"
  end
end

Then /^I should see the translation result "([^"]*)"$/ do |exp_translation_result|
  on @site, :results_page do |page|
    page.translation_result.gsub('colour', 'color').should == exp_translation_result
  end
end

Then /^I pause for a while$/ do
  sleep 10
end
