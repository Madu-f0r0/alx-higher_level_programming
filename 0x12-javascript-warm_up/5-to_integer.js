#!/usr/bin/node

const parsedNum = Number.parseInt(process.argv[2]);

if (!parsedNum)
{
        console.log("Not a number");
}
else
{
        console.log("My number: " + parsedNum);
}
