"""Service module 17336: business logic, no crypto."""


def calculate_total_17336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17336():
    return 'module 17336 handles orders and invoices'
