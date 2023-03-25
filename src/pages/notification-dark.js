import { Button } from "@chakra-ui/react";
import { ArrowForwardIcon } from "@chakra-ui/icons";

const NotificationDark = () => {
  return (
    <div className="relative bg-white w-full h-[79px] overflow-hidden text-left text-base text-white font-lato">
      <div className="absolute top-[0px] left-[0px] w-[1280px] h-[78.5px]">
        <div className="absolute top-[0px] left-[0px] bg-darkslategray-200 w-[1280px] h-[78.5px]" />
        <div className="absolute top-[19px] left-[33px] inline-block w-[924px] h-[39px]">{`Aenean sit amet magna vel magna fringilla fermentum. Donec sit amet nulla sed arcu pulvinar ultricies commodo id ligula. Nulla vehicula leo ut augue tincidunt, placerat tempus nulla rutrum. `}</div>
        <div className="absolute top-[20px] left-[1047px] w-[205px] h-[39px]">
          <Button
            className="absolute top-[0px] left-[0px]"
            variant="solid"
            w="205px"
            colorScheme="teal"
            rightIcon={<ArrowForwardIcon />}
          >
            ACCEPT
          </Button>
        </div>
      </div>
    </div>
  );
};

export default NotificationDark;
