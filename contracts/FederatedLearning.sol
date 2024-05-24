pragma solidity ^0.8.0;

contract FederatedLearning {
    struct ModelUpdate {
        address client;
        string updateHash;
    }

    ModelUpdate[] public updates;

    function submitUpdate(string memory updateHash) public {
        updates.push(ModelUpdate(msg.sender, updateHash));
    }

    function getUpdates() public view returns (ModelUpdate[] memory) {
        return updates;
    }
}
