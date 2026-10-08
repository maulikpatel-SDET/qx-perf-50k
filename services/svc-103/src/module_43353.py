"""Service module 43353: business logic, no crypto."""


def calculate_total_43353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43353():
    return 'module 43353 handles orders and invoices'
