const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
    });
}

const diffDate = (dateString) => {
    const dateNow = new Date()
    const date = new Date(dateString)

    const diffDate = dateNow - date

    let dateConverted = Math.floor(diffDate / (1000 * 60 * 60 * 24))

    if (dateConverted <= 0) return "hoje";
    if (dateConverted === 1) return "1d";
    if (dateConverted < 30) return `${dateConverted} d`;


    dateConverted = Math.floor(diffDays / 30);
    if (dateConverted === 1) return "1m";
    if (dateConverted < 12) return `${dateConverted}m`;

    dateConverted = Math.floor(diffDays / 365);
    if (diffYears === 1) return "1a";

    return dateConverted;

}



export { formatDate, diffDate }