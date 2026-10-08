"""Service module 27538: business logic, no crypto."""


def calculate_total_27538(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27538():
    return 'module 27538 handles orders and invoices'
