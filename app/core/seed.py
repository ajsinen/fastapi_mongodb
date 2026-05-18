from app.models.todo_model import TodoCategory

DEFAULT_CATEGORIES = [
    {"title": "Work", "description": "Office tasks, meetings, reports"},
    {"title": "Personal", "description": "Self-care, journaling, hobbies"},
    {"title": "Shopping", "description": "Groceries, supplies, wishlist"},
    {"title": "Health", "description": "Workout, appointments, medications"},
    {"title": "Finance", "description": "Budgeting, bills, savings"},
    {"title": "Household", "description": "Cleaning, repairs, laundry"},
    {"title": "Education", "description": "Study, courses, reading"},
    {"title": "Errands", "description": "Bank, post office, renewals"},
    {"title": "Social", "description": "Meet friends, calls, events"},
    {"title": "Travel", "description": "Plan trips, pack, bookings"},
]


async def seed_todo_categories():
    for category in DEFAULT_CATEGORIES:
        exists = await TodoCategory.find_one(category.get("title") == TodoCategory.title)
        if not exists:
            await TodoCategory(**category).insert()