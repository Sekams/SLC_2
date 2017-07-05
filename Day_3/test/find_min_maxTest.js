const expect = require('chai').expect;
  describe('Min-Max Numbers in a List: ', () => {

    describe('Return the min and max number in the list in a new list follows `[min, max]`', () => {

      it('should return [1,4] for [1, 2, 3 , 4]', () => {
        expect(findMinMax([1, 2, 3, 4])).to.be.deep.equal([1, 4]);
      });

      it('should return [4, 6] for [6, 4]', () => {
        expect(findMinMax([6, 4])).to.be.deep.equal([4, 6]);
      });

      it('should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]', () => {
        expect(findMinMax([4, 66, 6, 44, 7, 78, 8, 68, 2])).to.be.deep.equal([2, 78]);
      });

    });
  });


