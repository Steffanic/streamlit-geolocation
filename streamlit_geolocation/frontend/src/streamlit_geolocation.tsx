import {Streamlit,StreamlitComponentBase,withStreamlitConnection,} from "streamlit-component-lib";
import React, {ReactNode} from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLocationCrosshairs } from '@fortawesome/free-solid-svg-icons';

class Streamlit_geolocation extends StreamlitComponentBase {
    public render = (): ReactNode => {
    return(<button onClick={this.get_position}><FontAwesomeIcon icon={faLocationCrosshairs}/></button>);

}
private get_position = async () => {
    var position:GeolocationPosition = await new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject)
    });
    let coords = {"latitude": position.coords.latitude, "longitude": position.coords.longitude, "altitude": position.coords.altitude, "accuracy": position.coords.accuracy, "altitudeAccuracy": position.coords.altitudeAccuracy, "heading": position.coords.heading, "speed": position.coords.speed};
    Streamlit.setComponentValue(coords);
}
}

export default withStreamlitConnection(Streamlit_geolocation);