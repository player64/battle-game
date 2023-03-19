import axiosInstance from "@/axiosInstance";

export async function getPlayers(type = 'active') {

    let url
    switch (type) {
        case "active":
            url = '/get-players'
            break
        case "dead":
            url = '/get-dead-players'
            break
        default:
            return
    }

    try {
        const response = await axiosInstance.get(url);
        return response.data;
    } catch (error) {
        console.error(error);
    }
}