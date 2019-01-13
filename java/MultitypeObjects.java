/**
 * Collection of functions for multiple-type objects.
 * 
 * @author Jeffrey L.
 * @version 1.1
 * @since 2017-01-28
 */
public class MultitypeObjects {

	/**
	 * Returns the string of the class of a given object.
	 * 
	 * @param obj the input object.
	 * @return the string of the class of the object.
	 */
	public static String objectClass(Object obj) {
		final int beginClassIndex = 16;
		String objClass = "null";
		// if object is not null, getClass.
		if (obj != null) {
			objClass = obj.getClass().toString();
			objClass = objClass.substring(beginClassIndex);
		}
		// return the class string.
		return objClass;
	}

	/**
	 * Returns the string representation of the given object.
	 * 
	 * @param obj the input object
	 * @return the string representation of the object.
	 */
	public static String toString(Object obj) {
		String objString = (obj == null) ? "null" : obj.toString();
		return objString;
	}

	/**
	 * Returns true iff the given objects are of the same type.
	 * 
	 * @param obj1 the first input object.
	 * @param obj2 the second input object.
	 * @return true iff obj1 and obj2 are of the same type.
	 */
	public static boolean sameType(Object obj1, Object obj2) {
		// get the object classes of obj1 and obj2.
		String obj1Class = objectClass(obj1);
		String obj2Class = objectClass(obj2);
		// return true iff the classes are the same.
		return obj1Class.equals(obj2Class);
	}

	/**
	 * Returns true iff the given objects are equivalent in value.
	 * 
	 * @param obj1 the first input object.
	 * @param obj2 the second input object.
	 * @return true iff obj1 and obj2 are equivalent.
	 */
	public static boolean sameObjects(Object obj1, Object obj2) {
		boolean areSame = false;
		// if objects are same data types, compare them as strings.
		if (sameType(obj1, obj2)) {
			areSame = toString(obj1).equals(toString(obj2));
		}
		// return true iff the objects are of the same value.
		return areSame;
	}

}