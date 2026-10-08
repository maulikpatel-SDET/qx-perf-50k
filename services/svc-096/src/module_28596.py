"""Service module 28596: business logic, no crypto."""


def calculate_total_28596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28596():
    return 'module 28596 handles orders and invoices'
