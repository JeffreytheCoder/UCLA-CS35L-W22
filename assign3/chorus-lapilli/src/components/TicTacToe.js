import React, { useState } from 'react';

const Board = () => {
  const [winner, setWinner] = useState('');
  const [blocks, setBlocks] = useState(Array(9).fill(''));
  const [isNextX, setIsNextX] = useState(true);

  const getWinner = () => {
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
        setWinner(blocks[first]);
      }
    }
  };

  const handleClick = (i) => {
    if (winner || blocks[i]) {
      return;
    }

    const newBlocks = [...blocks];
    newBlocks[i] = isNextX ? 'X' : 'O';
    setBlocks(newBlocks);

    setIsNextX(!isNextX);
    getWinner();
  };

  return (
    <div class="flex flex-col font-mono">
      <div class="h-screen mt-20 items-center">
        <p class="mb-4">
          {winner
            ? `Winner: ${winner}`
            : isNextX
            ? 'Next player: X'
            : 'Next player: O'}
        </p>

        <div class="grid grid-cols-3 w-max mx-auto">
          {blocks.map((block, idx) => {
            return (
              <button
                class="border border-black w-20 h-20"
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
