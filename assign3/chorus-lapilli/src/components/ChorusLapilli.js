import React, { useEffect, useState } from 'react';
import useStateCallback from '../hooks/useStateCallback';

const Board = () => {
  const [winner, setWinner] = useState(null);
  const [blocks, setBlocks] = useState(Array(9).fill(''));
  const [isNextX, setIsNextX] = useState(true);

  const [steps, setSteps] = useState(0);
  const [selected, setSelected] = useState(-1);
  const [notice, setNotice] = useState('Place an X in an empty block');

  useEffect(() => {
    setWinner(getWinner(blocks));
  }, [steps]);

  useEffect(() => {
    if (winner) {
      setNotice(`Hoorah! Player ${winner} wins the game!`);
    }
  }, [winner]);

  const getWinner = (blocks) => {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];

    for (const line of lines) {
      const [first, second, third] = line;
      if (
        blocks[first] &&
        blocks[first] == blocks[second] &&
        blocks[second] == blocks[third]
      ) {
        return blocks[first];
      }
    }
    return null;
  };

  const getAvailableMoves = (i) => {
    switch (i) {
      case 0:
        return [1, 3, 4];
      case 1:
        return [0, 2, 3, 4, 5];
      case 2:
        return [1, 4, 5];

      case 3:
        return [0, 1, 4, 6, 7];
      case 4:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8];
      case 5:
        return [1, 2, 4, 7, 8];

      case 6:
        return [3, 4, 7];
      case 7:
        return [3, 4, 5, 6, 8];
      case 8:
        return [4, 5, 7];
    }
  };

  const handleClick = (i) => {
    if (winner) return;

    // deselect
    if (selected == i) {
      setNotice(`Select an ${isNextX ? 'X' : 'O'} to move`);
      setSelected(-1);
    }

    // move
    else if (selected != -1) {
      // check if the current block has been filled
      if (blocks[i]) {
        setNotice(
          `You must move the ${isNextX ? 'X' : 'O'} to an adjacent empty block!`
        );
      } else {
        // check if the current block is adjacent to the selected block
        for (const move of getAvailableMoves(selected)) {
          if (i == move) {
            // if the current player has a sign at the center, only move when the player can win
            const newBlocks = [...blocks];
            newBlocks[selected] = '';
            newBlocks[i] = isNextX ? 'X' : 'O';

            if (
              selected != 4 &&
              ((isNextX && blocks[4] == 'X') ||
                (!isNextX && blocks[4] == 'O')) &&
              !getWinner(newBlocks)
            ) {
              setNotice(
                `You can't win with this move! Either move the ${blocks[4]} at the center or find another way to win`
              );
            } else {
              setBlocks(newBlocks);

              setSelected(-1);
              setIsNextX(!isNextX);
              setSteps(steps + 1);

              setNotice(`Select an ${newBlocks[i] == 'X' ? 'O' : 'X'} to move`);
            }
            return;
          }
        }
        setNotice(
          `You must move the ${isNextX ? 'X' : 'O'} to an adjacent empty block!`
        );
      }
    }

    // select
    else if (steps >= 6) {
      // check if selected block is next player
      if ((isNextX && blocks[i] == 'X') || (!isNextX && blocks[i] == 'O')) {
        setSelected(i);
        setNotice(
          `Select an adjacent empty block to move to (click again to deselect)`
        );
      } else {
        setNotice(`You must select an ${isNextX ? 'X' : 'O'}!`);
      }
    }

    // place
    else {
      // check if current block has been filled
      if (blocks[i]) {
        setNotice(
          `You must place the ${isNextX ? 'X' : 'O'} in an empty block!`
        );
      } else {
        const newBlocks = [...blocks];
        newBlocks[i] = isNextX ? 'X' : 'O';
        setBlocks(newBlocks);

        const currentStep = steps;
        setSteps(steps + 1);
        setIsNextX(!isNextX);

        if (steps >= 5) {
          // if X at the center, give notice to move it
          if (newBlocks[4] == 'X') {
            setNotice('You have an X at the center! Select it to move');
          } else {
            setNotice(`Select an ${newBlocks[i] == 'X' ? 'O' : 'X'} to move`);
          }
        } else {
          setNotice(
            `Place an ${newBlocks[i] == 'X' ? 'O' : 'X'} in an empty block`
          );
        }
      }
    }
  };

  return (
    <div class="flex flex-col font-mono">
      <div class="h-screen mt-20 items-center">
        <p class="mb-4">Step: {steps}</p>
        <p class="mb-4">{notice}</p>

        <div class="grid grid-cols-3 w-max mx-auto">
          {blocks.map((block, idx) => {
            return (
              <button
                class={`border border-black w-20 h-20 ${
                  selected == idx ? 'border-4' : ''
                }`}
                key={idx}
                onClick={() => {
                  handleClick(idx);
                }}
              >
                <span>{blocks[idx]}</span>
              </button>
            );
          })}
        </div>

        {winner ? (
          <button
            class="mt-6 border border-black p-2 rounded"
            onClick={() => {
              setWinner('');
              setBlocks(Array(9).fill(''));
              setIsNextX(true);
              setSteps(0);
              setSelected(-1);
              setNotice('Place an X in an empty block');
            }}
          >
            Restart
          </button>
        ) : (
          <></>
        )}
      </div>
    </div>
  );
};

export default Board;
