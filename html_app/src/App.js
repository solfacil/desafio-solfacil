import {Button, Container, Form} from "react-bootstrap";
import {useRef} from "react";

function App() {
    const fileInput = useRef();

    const handlerSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append("file", fileInput.current.files[0]);
        const res = await fetch(process.env.REACT_APP_API_URL || "", {
            method: "POST",
            body: formData,
        });
        if (res.ok) {
            window.location.reload();
            console.log(await res.json());
        } else {
            alert("Error");
        }
    }
  return (
      <Container>
        <Form
            onSubmit={handlerSubmit}
            className={"d-flex justify-content-center align-items-center flex-column"}
        >
            <Form.Group className={"mb-3"} controlId="formBasicEmail">
                <Form.Label>File</Form.Label>
                <Form.Control type="file" multiple ref={fileInput}/>
            </Form.Group>

            <Button type={"submit"}>Upload</Button>
        </Form>
      </Container>
  );
}

export default App;
