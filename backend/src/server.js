const cors = require("cors");
const express = require("express");
const fs = require("node:fs");
const path = require("node:path");

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

app.get("/", (request, response) => {
  response.json({
    message: "Amp Stats Sweden API fungerar",
  });
});

app.get("/api/amputations", (request, response) => {
  const dataPath = path.join(
    __dirname,
    "..",
    "..",
    "data",
    "processed",
    "amputation_data.json"
  );

  if (!fs.existsSync(dataPath)) {
    return response.status(404).json({
      error: "Ingen bearbetad amputationsdata hittades ännu.",
    });
  }

  try {
    const fileContents = fs.readFileSync(dataPath, "utf-8");
    const data = JSON.parse(fileContents);

    return response.json(data);
  } catch (error) {
    console.error(error);

    return response.status(500).json({
      error: "Kunde inte läsa amputationsdatan.",
    });
  }
});

app.listen(PORT, () => {
  console.log(`API körs på http://localhost:${PORT}`);
});