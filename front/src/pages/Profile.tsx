import React                      from "react";
import {useDispatch, useSelector} from "react-redux";
import {useHistory}               from "react-router";
import authSlice                  from "../store/slices/auth";
import useSWR                     from 'swr';
import {fetcher}                  from "../utils/axios";
import {UserResponse}             from "../types/UserResponse";
// noinspection ES6UnusedImports
import {AccountResponse}          from "../types/AccountResponse";
import {RootState}                from "../store";


const Profile = () => {
    // TODO: types
    // @ts-ignore
    const account = useSelector ((state: RootState) => state.auth.account);
    const dispatch = useDispatch ();
    const history = useHistory ();
    // @ts-ignore
    const userId = account?.id;

    const user = useSWR<UserResponse> (`/user/${userId}/`, fetcher);

    const handleLogout = () => {
        // TODO: POTENTIAL PROBLEM, ARE WE USING A VOID RETURN VALUE??
        // TODO: DOES THE NESTED FUNCTION NEED A CALL VALUE??
        // noinspection JSVoidFunctionReturnValueUsed
        dispatch (authSlice.actions.setLogout ());
        history.push ("/login");
    };
    return (
        <div className="w-full h-screen">
            <div className="w-full p-6">
                <button
                    onClick={handleLogout}
                    className="rounded p-2 w-32 bg-red-700 text-white"
                >
                    Logout
                </button>
            </div>
            {
                user.data ?
                    <div className="w-full h-full text-center items-center">
                        <p className="self-center my-auto">Welcome, {user.data?.username}</p>
                    </div>
                    :
                    <p className="text-center items-center">Loading ...</p>
            }
        </div>
    );
};

export default Profile;
