"""Service module 2838: business logic, no crypto."""


def calculate_total_2838(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2838():
    return 'module 2838 handles orders and invoices'
