"""Service module 40235: business logic, no crypto."""


def calculate_total_40235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40235():
    return 'module 40235 handles orders and invoices'
