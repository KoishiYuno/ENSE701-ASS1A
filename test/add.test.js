var add = require('./add.js');
var expect = require('chai').expect;

describe('The unit test of add function', function() {
  it('1 + 1 should equal to 2', function() {
    expect(add(1, 1)).to.be.equal(2);
  });
});