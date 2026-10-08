"""Service module 15596: business logic, no crypto."""


def calculate_total_15596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15596():
    return 'module 15596 handles orders and invoices'
