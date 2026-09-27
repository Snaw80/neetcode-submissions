class LRUCache {
    private cache: Map<number,number> = new Map<number,number>
    private capacity: number
    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        let value: number | undefined = this.cache.get(key)
        if (!value){
            return -1
        }

        // reset order in the map
        this.cache.delete(key)
        this.cache.set(key,value)

        return value
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        if (this.cache.has(key)){
            this.cache.delete(key)
        }

        this.cache.set(key,value)

        if (this.cache.size > this.capacity)
        {
            const oldestKey = [...this.cache.keys()][0];
            if (oldestKey !== undefined) {
                this.cache.delete(oldestKey);
            }
        }
    }
}
