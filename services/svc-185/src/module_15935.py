"""Service module 15935: business logic, no crypto."""


def calculate_total_15935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15935():
    return 'module 15935 handles orders and invoices'
