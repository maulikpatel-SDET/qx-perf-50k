"""Service module 24235: business logic, no crypto."""


def calculate_total_24235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24235():
    return 'module 24235 handles orders and invoices'
