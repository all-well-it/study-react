import { Counter } from "./features/counter/Counter"
import "./App.css"
import { init } from "@twa.js/sdk"
import { Popup } from "@twa.js/sdk"

const popup = new Popup("6.3")

init().then((components) => {
  const { mainButton /*, viewport*/ } = components

  mainButton.on("click", () => {
    // viewport.expand()
    popup.open({
      title: "Hello!",
      message: "Here is a test message.",
      buttons: [{ id: "my-id", type: "default", text: "Default text" }],
    })
    console.log(popup.isOpened)
  })

  mainButton
    .setBackgroundColor("#70327b")
    .setTextColor("#ffffff")
    .setText("Expand!")
    .enable()
    .show()
})

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Counter />
      </header>
    </div>
  )
}

export default App
