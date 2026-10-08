"""Service module 34807: business logic, no crypto."""


def calculate_total_34807(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34807():
    return 'module 34807 handles orders and invoices'
