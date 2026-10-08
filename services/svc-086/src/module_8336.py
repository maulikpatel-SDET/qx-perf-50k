"""Service module 8336: business logic, no crypto."""


def calculate_total_8336(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8336():
    return 'module 8336 handles orders and invoices'
