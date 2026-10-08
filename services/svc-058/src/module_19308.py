"""Service module 19308: business logic, no crypto."""


def calculate_total_19308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19308():
    return 'module 19308 handles orders and invoices'
