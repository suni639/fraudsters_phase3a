// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FederatedLearning {
    struct ModelUpdate {
        address client;
        string parameters; // Serialized model parameters
    }

    ModelUpdate[] public updates;

    function submitUpdate(string memory parameters) public {
        updates.push(ModelUpdate({
            client: msg.sender,
            parameters: parameters
        }));
    }

    function getUpdate(uint _index) public view returns (address, string memory) {
        ModelUpdate storage update = updates[_index];
        return (update.client, update.parameters);
    }

    function getUpdatesCount() public view returns (uint) {
        return updates.length;
    }
}
