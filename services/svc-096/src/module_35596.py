"""Service module 35596: business logic, no crypto."""


def calculate_total_35596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35596():
    return 'module 35596 handles orders and invoices'
