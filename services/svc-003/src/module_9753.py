"""Service module 9753: business logic, no crypto."""


def calculate_total_9753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9753():
    return 'module 9753 handles orders and invoices'
