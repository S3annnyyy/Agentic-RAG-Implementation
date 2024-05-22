export function slideInFromLeft(delay: number) {
    return {
      hidden: { x: -100, opacity: 0},
      visible: {
        x: 0,
        opacity: 1,
        top: 0,
        transition: {
          delay: delay,
          duration: 0.5,
        },
      },
      exit: {x: -100, opacity: 0, transition: { delay: 0.5, duration: 0.5 } }
    };
  }
  
  export function slideInFromRight(delay: number) {
    return {
      hidden: { x: 100, opacity: 0 },
      visible: {
        x: 0,
        opacity: 1,
        transition: {
          delay: delay,
          duration: 0.5,
        },
      },
    };
  }
  
  export const slideInFromTop = {
    hidden: { y: -100, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        delay: 0.5,
        duration: 0.5,
      },
    },
  };

  export const slideInFromBottom = {
    hidden: { y: 100, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        delay: 0.5,
        duration: 0.5,
      },
    },
  };

  export const dropInFromTop = {
    hidden: {y: "-100vh"},
    visible: {
      y: "0",
      opacity: 1,
      transition: {
        duration: 0.1,
        type: "spring",
        daming: 25,
        stiffness: 500
      }
    },
    exit: {y: "100vh"},
  }